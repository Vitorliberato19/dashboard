#!/usr/bin/python3

import jenkins

jc = jenkins.Jenkins('http://192.168.0.200:8080')

# print(jc.get_whoami())
# print(jc.get_version())
# jc.create_job('421 - Exemplo',jenkins.EMPTY_CONFIG_XML)


# jc.build_job('Pipeline')


# for job in jc.get_jobs():
#     print(job['fullname'])

# xml = jc.get_job_config('Job')
# print(xml)

# with open('job.xml','r') as xml:
#     jc.reconfig_job('Job',xml.read())

jc.build_job('Job')


