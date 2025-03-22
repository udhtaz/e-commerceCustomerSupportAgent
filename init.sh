# clear
docker build -t conversational_agent:1.00 .
docker image ls
docker image rm -f $(docker images -f dangling=true -q)
docker run -p 8000:8000 conversational_agent:1.00