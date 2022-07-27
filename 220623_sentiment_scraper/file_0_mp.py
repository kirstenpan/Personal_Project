import socket

PATH = ''
on_vm = False
if socket.gethostname().find('ec2') != -1:
    on_vm = True
    PATH = 'civilience/2206_internship_program/220615_scraping_pipeline_final/'