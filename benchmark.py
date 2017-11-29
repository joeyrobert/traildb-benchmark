from os.path import basename, dirname, isfile, join
import subprocess
import sys
import urllib
from terminaltables import AsciiTable
from timeit import timeit

LANGUAGES = {
    'python-2.7': {
        'docker': 'python/Dockerfile.python2',
        'run': 'python benchmark.py'
    },
    'pypy': {
        'docker': 'python/Dockerfile.pypy',
        'run': 'pypy benchmark.py'
    },
    'crystal': {
        'docker': 'crystal/Dockerfile',
        'run': './benchmark'
    },
    'trck': {
        'docker': 'trck/Dockerfile',
        'run': './benchmark /mnt/data/wikipedia-history-small.tdb'
    },
    'c': {
        'docker': 'c/Dockerfile',
        'run': './benchmark'
    },
    'rust': {
        'docker': 'rust/Dockerfile',
        'run': 'benchmark'
    },
    'aholyoke-traildb-java': {
        'docker': 'java/Dockerfile.aholyoke',
        'run': 'java -Djava.library.path=/opt/traildb-java/native/linux/target/ -cp /opt/benchmark:/opt/traildb-java/native/linux/target/lib/traildbJava.jar Benchmark'
    },
    'haskell-fast': {
        'docker': 'haskell/Dockerfile',
        'run': './traildb-haskell-benchmark fast'
    },
    'haskell-pretty': {
        'docker': 'haskell/Dockerfile',
        'run': './traildb-haskell-benchmark pretty'
    },

    # NodeJS library is extremely slow, probably doing something silly
    # 'javascript': {
    #     'docker': 'javascript/Dockerfile',
    #     'run': 'node benchmark.js'
    # },

    # Library doesn't work on Python 3 yet
    # 'python-3.6': {
    #     'docker': 'python/Dockerfile.python3',
    #     'run': 'python benchmark.py'
    # },
    
    # Experiencing a fatal error
    # 'go': {
    #     'docker': 'go/Dockerfile',
    #     'run': 'go-wrapper run'
    # },
}

WIKI_URL = 'http://traildb.io/data/wikipedia-history-small.tdb'

def get_tag_name(key):
    return 'traildb-benchmark:{}'.format(key)

def get_language_dir(data):
    return join(dirname(__file__), dirname(data['docker']))

def get_docker_file(data):
    return join(get_language_dir(data), basename(data['docker']))

def download_wikipedia_traildb():
    if not isfile('wikipedia-history-small.tdb'):
        print 'Downloading Wikipedia from {}'.format(WIKI_URL)
        f = urllib.URLopener()
        f.retrieve(WIKI_URL, 'wikipedia-history-small.tdb')

def build_images(languages):
    for key, data in languages.iteritems():
        print 'Building docker container for {}'.format(key)
        language_dir = get_language_dir(data)
        docker_file = get_docker_file(data)
        tag_name = get_tag_name(key)
        cmd = ['docker', 'build', '-t', tag_name, '-f', docker_file, '.']
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        for line in iter(process.stdout.readline, ''):
            sys.stdout.write(line)

def run_benchmarks(languages, number=1):
    benchmarks = []
    for key, data in languages.iteritems():
        print 'Running benchmarks for {}'.format(key)
        tag_name = get_tag_name(key)
        cmd = ['docker', 'run', tag_name] + data['run'].split(' ')
        benchmark = timeit(stmt='subprocess.check_output({})'.format(cmd), setup='import subprocess', number=number)
        benchmarks.append({
            'duration': benchmark / number,
            'language': key
        })
    return benchmarks


def display_benchmarks(benchmarks):
    table_data = [['Position', 'Language', 'Average Duration']]
    benchmarks = sorted(benchmarks, key=lambda benchmark: benchmark['duration'])
    for i, benchmark in enumerate(benchmarks):
        table_data.append([i + 1, benchmark['language'], benchmark['duration']])
    print AsciiTable(table_data, title='TrailDB Benchmarks').table


if __name__ == '__main__':
    download_wikipedia_traildb()
    build_images(LANGUAGES)
    display_benchmarks(run_benchmarks(LANGUAGES, number=3))
