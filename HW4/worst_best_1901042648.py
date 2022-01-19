

def worst_best(success_rates, start , end):
    maxL = success_rates[start]
    maxR = success_rates[start]
    minL = success_rates[start]
    minR = success_rates[start]

    if start == end:
        return maxL, minL , start , start
    elif start - end == 1:
        if success_rates[start] > success_rates[end]:
            minL = success_rates[end]
            return maxL , minL , start , end
        else:
            maxL = success_rates[end]
            return maxL , minL , end , start       
    else:
        mid = int((start + end) / 2)
        maxL , minL , maxIndexL , minIndexL = worst_best(success_rates, start , mid)
        maxR , minR , maxIndexR , minIndexR = worst_best(success_rates, mid + 1 , end)
        return maxL if maxL >= maxR else maxR , minL if minL <= minR else minR , maxIndexL if maxL >= maxR else maxIndexR , minIndexL if minL <= minR else minIndexR

experiments = ['A',"B","C","D","E"]
success_rates = [50,10,90,14,67]

max , min , maxIndex , minIndex = worst_best(success_rates , 0 , len(success_rates) - 1)
print("Worst Experiment is",experiments[minIndex],"with",success_rates[minIndex],"success rate.")
print("Best Experiment is",experiments[maxIndex],"with",success_rates[maxIndex],"success rate.")