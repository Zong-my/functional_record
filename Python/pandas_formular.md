# DataFrame去重

## 1、根据某列去重

load.drop_duplicates(subset='time', keep='first', inplace=True)

## 2、根据索引去重

load = load[~load.index.duplicated(keep='first')]

# DataFrame排序

## 1、根据某列排序

load = load.sort_values(by="time", ascending=True)   #  ascending 升/降序

## 2、根据索引排序

load.sort_index(inplace=True)
