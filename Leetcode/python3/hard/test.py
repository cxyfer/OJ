model = lgb.LGBMRegressor(
    objective=qwk_obj,  # 設定 QWK 作為目標函數
    metrics='None',  # 不使用預設的 LightGBM 評分指標
    learning_rate=0.1,  # 學習率
    max_depth=5,  # 樹的最大深度
    num_leaves=10,  # 樹的葉子數量
    colsample_bytree=0.5,  # 每棵樹使用的特徵子集比例
    reg_alpha=0.1,  # L1 正則化
    reg_lambda=0.8,  # L2 正則化
    n_estimators=1024,  # 樹的數量
    random_state=42,  # 隨機種子
    verbosity=-1  # 禁用輸出信息
)