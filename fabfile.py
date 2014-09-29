from fabric.api import run
from fabric.operations import local


def clean():
    local('rm -rf ./deploy')

def fetch():
    local('scrapy crawl guokr -o spider/json/guokr_items.json')

def regen():
    clean()
    local('hyde -g -s .')


def serve():
    local('hyde -w -s .')


def host_type():
    run('uname -s')