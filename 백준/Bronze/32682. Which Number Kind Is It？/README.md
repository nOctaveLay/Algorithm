# [Bronze III] Which Number Kind Is It? - 32682 

[문제 링크](https://www.acmicpc.net/problem/32682) 

### 성능 요약

메모리: 111820 KB, 시간: 156 ms

### 분류

수학, 브루트포스 알고리즘

### 제출 일자

2025년 12월 4일 20:49:16

### 문제 설명

<p>There are many number kinds out there and I am sure you know some of them already! To name a few:</p>

<ul>
	<li>Odd number (<code>O</code>): $1, 3, 5, 7, 9, \ldots$</li>
	<li>Square number (<code>S</code>): $0, 1, 4, 9, 16, 25, \ldots$</li>
</ul>

<p>In this problem, you just need to output whether a given number $N$ is one of these special kinds of numbers. Print <code>O</code> if $N$ is odd, <code>S</code> if it's a perfect square, and <code>OS</code> if $N$ is both odd and a perfect square. If $N$ isn't either kind of special number, print <code>EMPTY</code> instead.</p>

### 입력 

 <p>The first line of input consists of an integer $T$ $(1 \leq T \leq 10^5)$, the number of test cases.</p>

<p>The remaining $T$ lines each contains a single integer $N$ $(0 \leq N \leq 10^6)$.</p>

### 출력 

 <p>Print $T$ lines, one per test case. On each line, print either <code>O</code> or <code>S</code> or <code>OS</code> or <code>EMPTY</code>, as described above.</p>

