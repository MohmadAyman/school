#!/bin/bash 
javac -cp :/usr/share/tomcat7/lib/servlet-api.jar *.java 
sudo cp *.class /usr/share/tomcat7-examples/examples/WEB-INF/classes
sudo cp *.html /var/lib/tomcat7/webapps/ROOT
sudo cp *.js /var/lib/tomcat7/webapps/ROOT
sudo cp *.css /var/lib/tomcat7/webapps/ROOT