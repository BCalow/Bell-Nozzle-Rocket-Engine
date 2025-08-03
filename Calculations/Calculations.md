# Calculations

## Table of Contents

 - [Nomenclature](#nomenclature)
 - [Heat Ratio of a Mutli-Comound Gas](#heat-ratio-of-a-multi-compound-gas-1)
 - [Stagnation Pressure](#stagnation-pressure-2)

## Nomenclature
<html>
<head>
<style> table, th, td {border: 1px solid white; border-collapse: collapse; text-align:center;} </style>
</script>
</head>

<body>
<table border="1" style="width: 50%; ">
  <tr>
    <th style="width:15%">Symbol</th>
    <th style="width:15%">Unit</th>
    <th style="width:70%">Meaning</th>
  </tr>

  <tr><td>γ</td><td>/</td><td>Ratio of Specific Heats</td></tr>
  <tr><td>mol%</td><td>/</td><td>Mole Percent</td></tr>
  <tr><td>P</td><td>Pa</td><td>Pressure</td></tr>
  <tr><td>M</td><td>/</td><td>Mach Number</td></tr>
</table>
</body>
</html>

### Heat Ratio of a Multi-Compound Gas <sup>[[1]](/Github/Bell-Nozzle-Rocket-Engine/Sources/Sources.md)</sup>

$\frac{1}{\gamma-1} = \displaystyle\sum_{} \frac{mol\%}{\gamma_i-1}$

### Stagnation Pressure <sup>[[2]](/Github/Bell-Nozzle-Rocket-Engine/Sources/Sources.md)</sup>

$P_s = P_1(1+\frac{\gamma-1}{2}M_1^2)^\frac{\gamma}{\gamma-1}$

### Area Ratio From Pressure

$\epsilon = \frac{(\frac{2}{\gamma+1})^\frac{1}{\gamma-1}(\frac{P_c}{P_e})^\frac{1}{\gamma}}{\sqrt{\frac{\gamma+1}{\gamma-1}(1-(\frac{P_e}{P_c})^\frac{\gamma-1}{\gamma})}}$