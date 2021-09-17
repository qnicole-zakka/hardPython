df.sample(n=x1, random_state=2021)
df.rename(columns={'a':1, 'b':2})
df.to_csv(f, index=False)
with open(Path(resp, 'loss_log'), 'a') as log:
            # write test performance to file 
            loss_w = csv.writer(loss_log)
            log_i = [epoch_n, cost_curr + ucost_curr]
            loss_w.writerow(log_i)
            
xgb_params = {}
    items = args['xgbParams'].split(',')
    for i in items:
        xgb_params[i.split(':')[0]] = float(i.split(':').strip())
    print('XGBoost parameters: ', xgb_params)
    print('Import training data...')
    train_data = pd.read_pickle(Path(datap, args['trainData']))
    X_train = train_data.drop(['__tag__'], axis=1).astype(float)#.values
    y_train = train_data['__tag__'].astype(float)#.values
    print('train: ', train_data.shape, 'feature type: ', type(X_train), X_train.shape, 'tag: ', y_train.shape)
    start_t = time.time()
    print('Xgboost training started at: ', datetime.datetime.fromtimestamp(start_t)) # epoch time to human readable
    clf = xgboost.XGBClassifier(**xgb_params)
    clf.fit(X_train, y_train)
    end_t = time.time()
    print('Xgboost training ended at: ', datetime.datetime.fromtimestamp(end_t))
    print('total time cost {} hours'.format((end_t - start_t) / 3600.0))
    # save the trained model
    pickle.dump(clf, open(Path(modelp, mod_f), 'wb'))
    print('Trained model saved to: ', Path(modelp, mod_f))
     y_pred_train = clf.predict(X_train)
    y_probas_train = clf.predict_proba(X_train)
    print('y_pred_train: ', y_pred_train.shape, ' y_probas_train: ', y_probas_train.shape)
    fig01, ax01 = plt.subplots()
    fpr_train, tpr_train, thr_train = roc_curve(y_train, y_probas_train[:, 1])
    skplt.metrics.plot_roc(y_train, y_probas_train, ax=ax01, plot_micro=False, classes_to_plot=[])
    thr_train[0] = 1
    roc_train = dict()
    roc_train['fpr'] = [0] + list(fpr_train) + [1]
    roc_train['tpr'] = [0] + list(tpr_train) + [1]
    roc_train['thr'] = [1] + list(thr_train) + [0]
    f_train = scipy.interpolate.interp1d(roc_train['fpr'], roc_train['tpr'])
    # TPR@{np.round(100*fpr):.0f}% = {f(fpr):.4f}
    print('recall@FPR=5% = {:.4f}'.format(f_train(0.05)))
    t_str_train = 'ROC Curve: Recall@FPR = ' + str(f_train(0.05)) 
    ax01.set_title(t_str_train)
    fig01.savefig(Path(resp, 'train_roc.png'))
    
    
