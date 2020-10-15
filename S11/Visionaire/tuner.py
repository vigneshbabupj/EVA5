

from torch_lr_finder import LRFinder
#from apex import amp


def findLR(model,train_loader,test_loader,criterion, optimizer,num_iteration):

    # Add this line before running `LRFinder`
    #model, optimizer = amp.initialize(model, optimizer, opt_level='O1')

    lr_finder = LRFinder(model, optimizer, criterion, device="cuda")
    lr_finder.range_test(train_loader, end_lr=0.5, num_iter=num_iteration) # fast ai method
    #lr_finder.range_test(train_loader, val_loader=test_loader, end_lr=10, num_iter = num_iteration, step_mode="linear")
    lr_finder.plot(log_lr=False)
    lr_finder.reset()
    
    best_lr = lr_finder.history['lr'][lr_finder.history['loss'].index(lr_finder.best_loss)]


    return best_lr