# Monograph-20-Examples
Worked examples from Monograph 20 'Phase Behavior' - Appendices B and C

These examples are all done inside Jupyter Notebooks, and will require some packages to be installed to run properly. If you receive a 'module not found' error message or some such, then this is generally the problem. For those new to Python, while there are a few ways to install packages the one I generally use is the pip installer.

Start a terminal window (or a DOS window for those on windows) and simply type 'pip install packagename'

Where packagename is the repository you want to install

The packages used are listed in `requirements.txt`, so you can install them all at once with:

    pip install -r requirements.txt

From memory, you should at least have the following installed;
- jupyter
- numpy
- scipy
- tabulate
- matplotlib

## pvt_utils.py

The component property library and the Peng-Robinson EOS / flash machinery that the
later examples share now live in a single module, `pvt_utils.py`, so each notebook
can import it rather than repeat the same code. It contains the component library,
the Hall-Yarborough Z-factor, Wilson K-values, the PR fugacity and flash routines, a
Michelsen stability test, and a robust Rachford-Rice solver (Nielsen & Lia, 2022).
Running `python pvt_utils.py` reproduces the published answers from Problem 18 as a
quick self-check.

Happy to receive suggestions for improvement

Mark
