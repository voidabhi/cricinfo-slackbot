

build: clean requirements copy tar

clean:
    @echo "Build started..."
    rm -rf dist dist.tar.gz
    
requirements:
	pip freeze > requirements.txt

copy:
    mkdir dist
    cp -R cricinfo.py dist
    cp requirements.txt dist

tar:
    @echo "Build completed..."
    tar -zc dist/ | gzip > dist.tar.gz

.PHONY: build
