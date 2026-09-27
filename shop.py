def Buy(item,count = 1):
    gamestate["Coins"] -= gamestate["Shop"][item]
    
def shop_renderer():
    pass