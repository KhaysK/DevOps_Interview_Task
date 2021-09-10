
# Interview project, Khabib Khaysadykov

<hr>
<h3>About project:</h3>
This project is an implementation of simple flask web application that shows current moscow time, dockerization of this applicatins and setting up ansible for deploy and laucnh this app on remote host.<br>
<br>Ansible will create directory in path <b>/home/$USER/interview</b> where it will copy web application and dockerfile<br>
<br>
1 - The main part of the project is ansible files, playbook and roles
<br>
2 - Flask web application and dockerfile are in roles/build_docker/files/interview 
<br>
<hr>
<h3>Host settings</h3>
<li>Before use you mast specify host data. In the file hosts you must specify address of host after equal sign</li>
<pre>
webhost ansible_host=[host address]
</pre>
<li>In group_vars/all you must specify connection settings after colon sign: user, password or ssh key (you can save ssh key into ssh_keys directory) </li>
<p style="margin-left: 40px">P.S. You can delete ansible_pass if you use ssh and vice versa
<pre>
ansible_user                  : 
ansible_pass                  :
ansible_ssh_private_key_file  :
</pre>