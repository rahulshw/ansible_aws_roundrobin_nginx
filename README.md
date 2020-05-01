# Objective: 
solve https://github.com/steeleye/recruitment-ext/wiki/SRE-Assessment

# How to use:
1. clone this repo
2. cd to its directory
3. run `pip install -r requirements.txt`. You can use a virtualenv if you want. 
4. get AWS access key and secret key from your aws account
5. save them in `env.example` and rename the file to `env`
6. run `source env`
4. run `ansible-playbook launch_ec2_within_VPC.yml`

# How to cleanup
1. go to AWS console
2. terminate all EC2 instances
3. delete the VPC
