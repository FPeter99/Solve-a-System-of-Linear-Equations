<p>Given a system of linear equations represented as:</p>

<p>A&sdot;x=B</p>

<p>Where:</p>

<ul>
	<li><code>A</code>&nbsp;is an n&times;n&nbsp;square matrix containing the coefficients of the equations.</li>
	<li><code>x</code> is the vector of unknowns to be determined.</li>
	<li><code>B</code>&nbsp;is the right-hand side vector containing the results of the equations.</li>
</ul>

<p>Your task is to solve for <code>x</code>, where <code>x</code> must be an integer vector. <strong>The solution vector must consist of integer values in all cases.</strong></p>

<p>&nbsp;</p>

<p><strong>Input:</strong></p>

<ul>
	<li>The matrix&nbsp;<code>A</code>of length n, where each sublist represents a row in the matrix <code>A</code>.</li>
	<li>A list <code>B</code> of length n, representing the right-hand side vector <code>B</code>.</li>
</ul>

<p><strong>Output:</strong></p>

<ul>
	<li>If the system has a unique integer solution, return the solution vector <code>x</code>.</li>
	<li>If there is no unique solution (for example, if the matrix is singular or the system has no solutions), return an empty list <code>[]</code>.<br />
	&nbsp;</li>
</ul>

<p><strong>Example 1</strong></p>

<blockquote>
<p><strong>Input:&nbsp;</strong>A = [[1, 1], [1, -1]], B = [3, 1]</p>

<p><strong>Output:&nbsp;</strong>[2, 1]</p>

<p><strong>Explanation:&nbsp;</strong>1*2 + 1*1 = 3, 1*2 - 1*1 = 1</p>
</blockquote>

<p><strong>Example 2:</strong></p>

<blockquote>
<p><strong>Input:&nbsp;</strong>A = [[1, 2], [3, -5]], B = [4, 1]</p>

<p><strong>Output:&nbsp;</strong>[2, 1]</p>

<p><strong>Explanation:&nbsp;</strong>1*2 + 2*1 = 4, 3*2 + (-5*1) = 1<br />
&nbsp;</p>

<p><img alt="" src="https://github.com/FPeter99/Solve-a-System-of-Linear-Equations/blob/main/Visualization.JPG?raw=true" /></p>
</blockquote>

<p><strong>Example 3:</strong></p>

<blockquote>
<p><strong>Input:&nbsp;</strong>A = [[1, 1], [0, 0]], B = [4, 1]</p>

<p><strong>Output:&nbsp;</strong>[]</p>

<p><strong>Explanation:&nbsp;</strong>0*x + 0*y != 1<br />
&nbsp;</p>
</blockquote>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>A</code> is an n x n matrix</li>
	<li><code>2 &lt;= A[i].length&nbsp;&lt;= 30</code></li>
	<li><code>0 &lt;= A[i][j] &lt;= 100&nbsp;</code></li>
	<li><code>B.Length&nbsp;= A[i]</code></li>
	<li>The solution, if it exists, must always be an integer.</li>
</ul>

<p>&nbsp;</p>
