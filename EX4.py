SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
OUTROS = 19849.53

SOMA = (SP+RJ+MG+ES+OUTROS)

SP_P = (SP*100/SOMA)
RJ_P = (RJ*100/SOMA)
MG_P = (MG*100/SOMA)
ES_P = (ES*100/SOMA)
OUTROS_P = (OUTROS*100/SOMA)

print ("SP tem %.2f" % SP_P,'% do faturamento')
print("RJ tem %.2f" % RJ_P,'% do faturamento')
print("MG tem %.2f" % MG_P,'% do faturamento')
print("ES tem %.2f" % ES_P,'% do faturamento')
print("OUTROS tem %.2f" % OUTROS_P,'% do faturamento')