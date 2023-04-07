<html>
<head>
<title>practic 17.7.3.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #a9b7c6;}
.s1 { color: #6a8759;}
.s2 { color: #6897bb;}
.s3 { color: #cc7832;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
practic 17.7.3.py</font>
</center></td></tr></table>
<pre><span class="s0">money = float(input(</span><span class="s1">'money : '</span><span class="s0">))</span>
<span class="s0">per_cent = {</span><span class="s1">'ТКБ'</span><span class="s0">: </span><span class="s2">5.6</span><span class="s3">, </span><span class="s1">'СКБ'</span><span class="s0">: </span><span class="s2">5.9</span><span class="s3">, </span><span class="s1">'ВТБ'</span><span class="s0">: </span><span class="s2">4.28</span><span class="s3">, </span><span class="s1">'СБЕР'</span><span class="s0">: </span><span class="s2">4.0</span><span class="s0">}</span>
<span class="s0">deposit = [r * (money / </span><span class="s2">100</span><span class="s0">) </span><span class="s3">for </span><span class="s0">r </span><span class="s3">in </span><span class="s0">per_cent.values()]</span>

<span class="s0">print(</span><span class="s1">'deposit''='</span><span class="s3">, </span><span class="s0">deposit</span><span class="s3">, </span><span class="s1">'руб'</span><span class="s0">)</span>
<span class="s0">deposit_max = max(deposit)</span>

<span class="s0">print(</span><span class="s1">'Максимальная сумма, которую вы можете заработать'</span><span class="s3">,</span><span class="s1">'—'</span><span class="s3">, </span><span class="s0">deposit_max</span><span class="s3">, </span><span class="s1">'руб'</span><span class="s0">)</span></pre>
</body>
</html>