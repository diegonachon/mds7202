def select_columns(X):
    features_selected = ['MinMaxScaler__CreditCap', 'MinMaxScaler__BankSpots8w', 'MinMaxScaler__HustleMinutes', 'MinMaxScaler__RiskScore', 
                         'MinMaxScaler__ZipHustle', 'MinMaxScaler__Speed4w', 'MinMaxScaler__BankMonths', 'MinMaxScaler__DOBEmails4w', 'MinMaxScaler__intended_balcon_amount', 
                         'MinMaxScaler__NewCribMonths', 'MinMaxScaler__Speed6h', 'MinMaxScaler__customer_age', 'StandardScaler__Speed24h', 'RobustScaler__DaysSinceJob', 
                         'RobustScaler__OldHoodMonths', 'OneHot__JobStatus_CA', 'OneHot__JobStatus_CB', 'OneHot__CribStatus_BA', 'OneHot__CribStatus_BB', 
                         'OneHot__CribStatus_BC', 'OneHot__CribStatus_BE', 'OneHot__LootMethod_AA', 'OneHot__LootMethod_AB', 'OneHot__LootMethod_AC',
                         'OneHot__DeviceOS_linux', 'OneHot__DeviceOS_other', 'OneHot__DeviceOS_windows', 'Pasthrough__AliveSession', 'Pasthrough__AliasMatch', 
                         'Pasthrough__DeviceEmails8w', 'Pasthrough__income', 'Pasthrough__FreeMail', 'Pasthrough__HomePhoneCheck', 'Pasthrough__ExtraPlastic']
    return X[features_selected]
