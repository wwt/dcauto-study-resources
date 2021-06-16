# Development Dockerfile for WWT - Cisco DevNet DCAUTO Study Resources

FROM python:3.9-slim-buster

LABEL maintainer="Tim Hull <tim.hull@wwt.com>"

WORKDIR /app

# TCP 8000 for MkDocs server
EXPOSE 8000/tcp

# TCP 8888 for Jupyter Lab Server
EXPOSE 8888/tcp

# Update repositories and install Git
RUN apt-get update && \
    apt-get install -y git

# Copy requirements files to Image
COPY requirements/ requirements/

# Install Python packages and Ansible Collections
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements/requirements.txt && \
    ansible-galaxy collection install -r requirements/ansible-galaxy.yml

# Install and configure PowerShell
RUN dpkg -i requirements/ucs/packages-microsoft-prod.deb && \
    apt-get update && \
    apt-get install -y powershell && \
    ./requirements/ucs/ucs-powertool-setup.sh

# Run script to launch server services
ENTRYPOINT [ "./requirements/server-launch.sh" ]

CMD [ "/bin/bash" ]
