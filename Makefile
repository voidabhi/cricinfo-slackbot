

build: clean requirements copy tar

clean:
    @echo "Build started..."
    rm -rf dist dist.tar.gz
    
requirements:
    @echo "Freezing pip requirements.."
    pip freeze > requirements.txt

copy:
    @echo "Create dist directory..."
    mkdir dist
    cp cricinfo.py dist
    cp requirements.txt dist
    cp runtime.txt dist

tar:
    @echo "Build completed..."
    tar -zc dist/ | gzip > dist.tar.gz

.PHONY: build
