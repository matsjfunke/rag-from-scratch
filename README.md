[More on how I personally think about the algorithms here](ALGORITHMS.md)

# How to experiment with the scripts

1. **clone repo**
   ```bash
   git clone
   ```
2. **install dependences**
   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```
3. **run scripts**
   - will take some time on the first run because embeddings aren’t cached (have a look at the handle_embeddings() function to understand)
   - you have to run it twice if the embeddings are not saved as json yet
   ```bash
   python dot-product-rag.py
   ```
5. **tinkering optiions**
   - each script contains a main() function this function gives you inside on tweaks you can make
   - different data: upload other .txt files in the root dir of the repo and specify thier name in file_name variable of main()
   - different prompt: change prompt vairable in main()
