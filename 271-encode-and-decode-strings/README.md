<h2><a href="https://leetcode.com/problems/encode-and-decode-strings">Encode and Decode Strings</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Design an algorithm to <strong>encode</strong> a list of strings into a single string. The encoded string is sent over the network and is <strong>decoded</strong> back into the original list of strings.</p>

<p>The tricky part is that <code>strs[i]</code> can contain <strong>any possible characters</strong>, so the encoding must avoid ambiguity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">dummy_input = [&quot;Hello&quot;,&quot;World&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[&quot;Hello&quot;,&quot;World&quot;]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Machine 1 encodes the list into a single string message.</li>
	<li>Machine 2 decodes that message back into the same list of strings.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">dummy_input = [&quot;&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[&quot;&quot;]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= strs.length &lt; 100</code></li>
	<li><code>0 &lt;= strs[i].length &lt; 200</code></li>
	<li><code>strs[i]</code> contains any possible characters out of 256 valid ASCII characters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you write a generalized algorithm to work on any possible set of characters?</p>
