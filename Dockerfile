
FROM continuumio/miniconda3

LABEL Name=conda-docker-sample Version=0.0.1
WORKDIR /app
ADD . /app


RUN conda env create -f environment.yml
RUN conda install -c conda-forge geckodriver
CMD /bin/bash -c "source activate myenv && python3 -m scraper" 
