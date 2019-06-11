import os
from tld import get_fld
import urllib.request
import io

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


def get_domain_name(url):
    domain_name = get_fld(url)
    return domain_name


def get_ip_address(url):
    command = "host " + url
    process = os.popen(command)
    results = str(process.read())
    line = results.find("has address") + 12

    return results[line:].splitlines()[0]

def get_nmap(ip):
    command = "namp -F " + ip
    process = os.popen(command)
    results = str(process.read())

    return results


def get_robots(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + "/"

    request = urllib.request.urlopen(path + "robots.txt", data = None)
    data = io.TextIOWrapper(request, encoding='utf-8')
    return data.read()


def get_whois(url):
    command = "whois " + url
    process = os.popen(command)
    results = str(process.read())
    return results
