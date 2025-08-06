class demotrading:
    def __init__(self,id, Asset, position_type, entryprice, stoploss, takeprofit, Risk_in_percent, RR_ratio,
                 size_in_asset, strategy_used, strategy_compliance, thoughts_before, thoughts_during, thoughts_after,
                 exit_price, PNL):
        self.id = id
        self.Asset = Asset
        self.position_type = position_type
        self.entryprice = entryprice
        self.stoploss = stoploss
        self.takeprofit = takeprofit
        self.Risk_in_percent = Risk_in_percent
        self.RR_ratio = RR_ratio
        self.size_in_asset = size_in_asset
        self.strategy_used = strategy_used
        self.strategy_compliance = strategy_compliance
        self.thoughts_before = thoughts_before
        self.thoughts_during = thoughts_during
        self.thoughts_after = thoughts_after
        self.exit_price = exit_price
        self.PNL = PNL

    def __str__(self):
         return (
             f"id: {self.id}\n"
             f"Asset: {self.Asset}\n"
             f"position_type: {self.position_type}\n"
             f"entryprice: {self.entryprice}\n"
             f"stoploss: {self.stoploss}\n"
             f"takeprofit: {self.takeprofit}\n"
             f"Risk_in_percent: {self.Risk_in_percent}\n"
             f"RR_ratio: {self.RR_ratio}\n"
             f"size_in_asset: {self.size_in_asset}\n"
             f"strategy_used: {self.strategy_used}\n"
             f"strategy_compliance: {self.strategy_compliance}\n"
             f"thoughts_before: {self.thoughts_before}\n"
             f"thoughts_during: {self.thoughts_during}\n"
             f"thoughts_after: {self.thoughts_after}\n"
             f"exit_price: {self.exit_price}\n"
             f"PNL: {self.PNL}\n"
         )
    def input(self):
        self.id = int(input("Input trade number: "))
        self.Asset = input("Input asset (e.g. ETH): ")
        self.position_type = bool(int(input("Position type (1 = long, 0 = short): ")))
        self.entryprice = float(input("Entry price: "))
        self.stoploss = float(input("Stop loss: "))
        self.takeprofit = float(input("Take profit: "))
        self.Risk_in_percent = float(input("Risk in %: "))
        self.RR_ratio = float(input("Risk-Reward ratio: "))
        self.size_in_asset = float(input("Size in asset: "))
        self.strategy_used = input("Strategy used: ")
        self.strategy_compliance = bool(int(input("Strategy compliance (1 = yes, 0 = no): ")))
        self.thoughts_before = input("Thoughts before trade: ")
        self.thoughts_during = input("Thoughts during trade: ")
        self.thoughts_after = input("Thoughts after trade: ")
        self.exit_price = float(input("Exit price: "))
        self.PNL = float(input("Profit/Loss with (+/-): "))

    def output(self):
        print(f"id: {self.id}")
        print(f"Asset: {self.Asset}")
        print(f"position_type: {self.position_type}")
        print(f"entryprice: {self.entryprice}")
        print(f"stoploss: {self.stoploss}")
        print(f"takeprofit: {self.takeprofit}")
        print(f"Risk_in_percent: {self.Risk_in_percent}")
        print(f"RR_ratio: {self.RR_ratio}")
        print(f"size_in_asset: {self.size_in_asset}")
        print(f"strategy_used: {self.strategy_used}")
        print(f"strategy_compliance: {self.strategy_compliance}")
        print(f"thoughts_before: {self.thoughts_before}")
        print(f"thoughts_during: {self.thoughts_during}")
        print(f"thoughts_after: {self.thoughts_after}")
        print(f"exit_price: {self.exit_price}")
        print(f"PNL: {self.PNL}")

    def set_id(self, id): self.id = id

    def get_id(self): return self.id

    def set_Asset(self, Asset): self.Asset = Asset

    def get_Asset(self): return self.Asset

    def set_position_type(self, position_type): self.position_type = position_type

    def get_position_type(self): return self.position_type

    def set_entryprice(self, entryprice): self.entryprice = entryprice

    def get_entryprice(self): return self.entryprice

    def set_stoploss(self, stoploss): self.stoploss = stoploss

    def get_stoploss(self): return self.stoploss

    def set_takeprofit(self, takeprofit): self.takeprofit = takeprofit

    def get_takeprofit(self): return self.takeprofit

    def set_Risk_in_percent(self, Risk_in_percent): self.Risk_in_percent = Risk_in_percent

    def get_Risk_in_percent(self): return self.Risk_in_percent

    def set_RR_ratio(self, RR_ratio): self.RR_ratio = RR_ratio

    def get_RR_ratio(self): return self.RR_ratio

    def set_size_in_asset(self, size_in_asset): self.size_in_asset = size_in_asset

    def get_size_in_asset(self): return self.size_in_asset

    def set_strategy_used(self, strategy_used): self.strategy_used = strategy_used

    def get_strategy_used(self): return self.strategy_used

    def set_strategy_compliance(self, strategy_compliance): self.strategy_compliance = strategy_compliance

    def get_strategy_compliance(self): return self.strategy_compliance

    def set_thoughts_before(self, thoughts_before): self.thoughts_before = thoughts_before

    def get_thoughts_before(self): return self.thoughts_before

    def set_thoughts_during(self, thoughts_during): self.thoughts_during = thoughts_during

    def get_thoughts_during(self): return self.thoughts_during

    def set_thoughts_after(self, thoughts_after): self.thoughts_after = thoughts_after

    def get_thoughts_after(self): return self.thoughts_after

    def set_exit_price(self, exit_price): self.exit_price = exit_price

    def get_exit_price(self): return self.exit_price

    def set_PNL(self, PNL): self.PNL = PNL

    def get_PNL(self): return self.PNL

    def print_trade_feature(self,feature):
        try:
            print(f"{feature}:{getattr(self,feature)}")
        except AttributeError:
            print(f"feature: {feature} doesnt exist" )

    def to_sql_dict(self):
        return {
            "id": self.id,
            "Asset": self.Asset,
            "position_type": self.position_type,
            "entryprice": self.entryprice,
            "stoploss": self.stoploss,
            "takeprofit": self.takeprofit,
            "Risk_in_percent": self.Risk_in_percent,
            "RR_ratio": self.RR_ratio,
            "size_in_asset": self.size_in_asset,
            "strategy_used": self.strategy_used,
            "strategy_compliance": self.strategy_compliance,
            "thoughts_before": self.thoughts_before,
            "thoughts_during": self.thoughts_during,
            "thoughts_after": self.thoughts_after,
            "exit_price": self.exit_price,
            "PNL": self.PNL
        }

