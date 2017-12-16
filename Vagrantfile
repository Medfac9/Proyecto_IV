Vagrant.configure("2") do |config|
  config.vm.box = "dummy"

  config.vm.define "bot-track-aws" do |host|
    host.vm.hostname = "bot-track-aws"
  end
  config.vm.provider :aws do |aws, override|
    aws.access_key_id = "ASIAIB4EFTNW4Z3L5FKA"
    aws.secret_access_key = "faGv5Ah5wlb80ZUeHXDwPpG5OCUIjnAo1jzoG5nR"
    aws.session_token = "FQoDYXdzEHwaDHMQQ9r5ZLkDlXr9UiKUATRo9cKTdfmtk8SPpAZmdwydEO52i/Z3P301bPaK/TpN58b/bGUEmR2YndxKjfmSx7mXpKSvE1DbmSJVUNf+td3AbzPaAOjDTccHQfkitfwzmUsVpwEJaptgRSRTjMoAEg38BJkvt5bxbJu5RRUiwLt3K3cn8IPENltMyFVoss5/zvtZTYKKrqlLBXTbvTH5MMFdjQEo8NvV0QU="
    aws.keypair_name = "KEY"
    aws.region= "us-west-2"
    aws.security_groups = [ 'grupo' ]
    aws.instance_type= 't2.micro'
    aws.ami = "ami-19e92861"

    override.ssh.username = "ubuntu"
    override.ssh.private_key_path = "/Users/mrmedfac9/Downloads/KEY.pem"
  end

    config.vm.provision :ansible do |ansible|
    	ansible.playbook = "ansible_bot.yml"
    	ansible.force_remote_user= true
    	ansible.host_key_checking=false
  end

end