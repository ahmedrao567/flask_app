First i run a project simple flask app 
then pushed it to github
then i make a jenkins ci cd pipeline for automation of building our app and then testins and then deploying
before that i make an image of my project and make a conatiner 
that pipeline when on build send that image to docker hub
then  rocky server pulles that image and then deply or run on that
now configured a webhook for triggering the autoamtion build of jenkins to automatically deploy my project whenver i push code to a github

challenges i faced 
the challenges i faced are alot
pipeline issue occur it says git is not working then i setup the git in jenkins container 
then issue occur about the public url payload url then i use ngrok that provides public url for webhook it takes alot of my time 
then on deployment stage i occur and issue of port then i changed the port bcz it was already in use and changes all the port in app in pipeline etc 
thats all challenegs that i face
.