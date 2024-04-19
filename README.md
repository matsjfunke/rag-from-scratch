# Algorithms

1. **Dot product** 
    - The dot product is used to find the angle between two vectors and to project one vector onto another, it provides a way to measure the similarity or alignment between two vectors.
    - Formula:
        - Multiply each dimension from vector \( \mathbf{a} \) and \( \mathbf{b} \) and add up the products:
        \[
        \mathbf{a} \cdot \mathbf{b} = a_1 b_1 + a_2 b_2 + \cdots + a_n b_n
        \]

2. **Cosine similarity**
    - Divides the angle of the two vectors (dot product) by the length (magnitude) of the vectors.
    - Think of it as concatenated Pythagorean theorems:
    \[ \|A\| = \sqrt{a_1^2 + a_2^2 + \cdots + a_n^2} \]
    - Formula:
    \[
    \text{cosine\_similarity}(A, B) = \frac{{\mathbf{A} \cdot \mathbf{B}}}{{\|A\| \|B\|}}
    \]

3. **Euclidean Distance**
    - Measure of the straight-line distance between two points (vector heads in this use case).
    - Formula:
    \[ d(P,Q) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + \cdots + (z_2 - z_1)^2} \]

4. **Manhattan Distance**
    - Distance between two points in a grid-based system. 
    - It's named as such because it measures the distance a taxi would have to travel on a grid-like street network.
    - Formula:
    \[ d = |x_2 - x_1| + |y_2 - y_1| + |z_2 - z_1| + |w_2 - w_1| \]

[great article on vector similarity algorithms](https://medium.com/@serkan_ozal/vector-similarity-search-53ed42b951d9)
