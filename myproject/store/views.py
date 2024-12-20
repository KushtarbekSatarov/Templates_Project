from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Goods, Feedback
from .forms import GoodsForm

def goods_list(request):
    goods = Goods.objects.all()
    return render(request, 'goods_list.html', {'goods':goods})


def goods_detail(request, pk):
    goods = get_object_or_404(Goods,pk=pk)
    feedback_list = Feedback.objects.filter(goods=goods)
    return render(request, 'goods_detail.html', {'goods':goods, 'feedback_list': feedback_list})


def goods_create(request):
    if request.method == 'POST':
        form = GoodsForm(request.POST, request.FILES)
        if form.is_valid():
            goods = form.save()
            return redirect('goods_detail', pk=goods.pk)
    else:
        form = GoodsForm()
    return render(request, 'goods_create.html', {'form':form})

def goods_update(request, pk):
    goods = get_object_or_404(Goods, pk=pk)
    if request.method == "POST":
        form = GoodsForm(request.POST, request.FILES, instance=goods)
        if form.is_valid():
            goods = form.save()
            return redirect('goods_detail', pk=goods.pk)
    else:
        form = GoodsForm(instance=goods)
    return render(request, 'goods_update', {'form':form, 'goods':goods})
