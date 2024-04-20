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
   ```bash
   python dot-product-rag.py
   ```
5. **tinkering optiions**
   - each script contains a main() function this function gives you inside on tweaks you can make
   - different data: upload other .txt files in the root dir of the repo and specify thier name in file_name variable of main()
   - different prompt: change prompt vairable in main()


# Algorithms
Algorithms are implemented in get_similar_chunks() function

1. **Dot product** 
    - The dot product is used to find the angle between two vectors and to project one vector onto another, it provides a way to measure the similarity or alignment between two vectors.
    - Formula:
        - Multiply each dimension from vector a and b and add up the products:
        ```
        a * b = a1 * b1 + a2 * b2 + ... + an * bn
        ```

2. **Cosine similarity**
    - Divides the angle of the two vectors (dot product) by the length (magnitude) of the vectors.
    - Think of it as concatenated Pythagorean theorems:
        - Magnitude of vector A:
        ```
        |A| = sqrt(a1^2 + a2^2 + ... + an^2)
        ```
    - Formula:
        ```
        cosine_similarity(A, B) = (A dot B) / (|A| * |B|)
        ```

3. **Euclidean Distance**
    - Measure of the straight-line distance between two points (vector heads in this use case).
    - Think walking from vector endpoint the other.
    - Formula:
        ```
        d(P,Q) = sqrt((x2 - x1)^2 + (y2 - y1)^2 + ... + (zn - z1)^2)
        ```

4. **Manhattan Distance**
    - Distance between two points in a grid-based system. 
    - It's named as such because it measures the distance a taxi would have to travel on a grid-like street network.
    - Think about it like walking along both vectors, changing direction for each dimension.
    - Formula:
        ```
        d = |x2 - x1| + |y2 - y1| + ... + |wn - wn|
        ```

5. **Mats simple formula**
    - Formula:
        ```
        d = (x2 - x1) + (y2 - y1) + ... + (wn - wn)
        ```

[great article on vector similarity algorithms](https://medium.com/@serkan_ozal/vector-similarity-search-53ed42b951d9)
