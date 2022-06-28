import tomotopy as tp

def lda_train (text) :
    mdl = tp.LDAModel(k=1) # num of topics

    for line in open('modelling/sample.txt'):
        print(line.strip().split())
        mdl.add_doc(line.strip().split())

    mdl.add_doc(text.strip().split())

    for i in range(0, 100, 10):
        mdl.train(10)
        print('Iteration: {}\tLog-likelihood: {}'.format(i, mdl.ll_per_word))

    for k in range(mdl.k):
        print('Top 10 words of topic #{}'.format(k))
        print(mdl.get_topic_words(k, top_n=10))

    mdl.summary()


