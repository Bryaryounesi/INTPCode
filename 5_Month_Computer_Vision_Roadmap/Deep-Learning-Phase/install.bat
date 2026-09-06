@echo off
call venv\Scripts\activate
echo Installing all packages from local wheels...
pip install --no-index --find-links=wheels torch==2.5.1+cpu torchaudio==2.5.1+cpu torchvision==0.20.1+cpu sympy==1.13.1 mpmath==1.3.0 jinja2==3.1.6 MarkupSafe==3.0.3 networkx==3.6.1 filelock typing-extensions fsspec setuptools
pip install --no-index --find-links=wheels contourpy==1.3.3 cycler==0.12.1 fonttools==4.64.0 kiwisolver==1.5.1 matplotlib==3.11.1 numpy==2.5.2 opencv-python==5.0.0.93 packaging==26.3 pandas==3.0.5 pillow==12.3.0 pyparsing==3.3.2 python-dateutil==2.9.0.post0 six==1.17.0 tzdata==2026.3
echo Done!
pause