'''
Created on 2018年2月22日

@author: chenshen
'''

import os
from flaskp import app

def main():
	return app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
	main()
    
