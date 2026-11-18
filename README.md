# authentication-security-lab
an Authentication &amp; Password Security Testing Lab using Kali Linux and Ubuntu Server

# Run -> password_auditor

  _> python3 password_auditor.py

# Run -> auth_log_analyzer

  - On ubuntu :
     /var/log/auth.log
    
  - can copy the relevant log into a file accessible to your normal user:
    
      sudo cp /var/log/auth.log ~/auth.log
      sudo chown "$USER":"$USER" ~/auth.log

   _> python3 auth_log_analyzer.py ~/auth.log

# Run -> shh_config_audit

  _> chmod +x ssh_config_audit.sh
    ./ssh_config_audit.sh

# Run -> ssh_login_test
  _> chmod +x ssh_login_test.sh
      ./ssh_login_test.sh
