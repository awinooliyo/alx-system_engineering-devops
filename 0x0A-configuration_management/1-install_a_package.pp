# Installing flask from pip3.
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Install Werkzeug 2.1.1
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

# Install python3-pip
package { 'python3-pip':
  ensure   => 'present',
}
