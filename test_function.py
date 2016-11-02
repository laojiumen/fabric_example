#!/usr/bin/env python
# coding=utf-8
from fabric.api import env, cd, local, put, env, get, run, sudo


env.hosts = ['vagrant@192.168.33.100']

def test_local():
    local('cd /tmp && touch a.txt')


def test_scp():
    # update support regular
    put('/tmp/a.txt', '/tmp')
    # download support regular
    get('/tmp/a.tx*', 'server1')


def test_remote_operate():
    with cd('/tmp'):
        run('mv a.txt b.txt')


# sudo
def test_sudo():
    sudo('touch /tmp/c.txt')
