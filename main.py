from file import *

ROOT = 'targets'

create_dir(ROOT)


def gather_data(name, url):
    robots_txt = get_robots(url)
    domain_name = get_domain_name(url)
    whois = get_whois(domain_name)
    ip = get_ip_address(domain_name)
    nmap = get_nmap(ip)

    report(name, url, domain_name, nmap, robots_txt, whois)


def report(name, url, domain_nmae, nmap, robots_txt, whois):
    project_dir = ROOT + "/" + name
    create_dir(project_dir)
    write_file(project_dir + "/url.txt", url)
    write_file(project_dir + "/domain_name.txt", domain_nmae)
    write_file(project_dir + "/nmap.txt", nmap)
    write_file(project_dir + "/robots.txt", robots_txt)
    write_file(project_dir + "/whois.txt", whois)


gather_data("google", "https://www.google.com/")

print("Scan Completed !!")
