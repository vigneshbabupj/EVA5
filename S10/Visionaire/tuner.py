



from torch_lr_finder import LRFinder



def findLR(model,criterion, optimizer,trainloader):

    lr_finder = LRFinder(model, optimizer, criterion, device="cuda")
    lr_finder.range_test(trainloader, end_lr=100, num_iter=100)
    lr_finder.plot() # to inspect the loss-learning rate graph
    lr_finder.reset() # to reset the model and optimizer to their initial state