$(document).ready(function(){
    $('.filter-checkbox,#PriceFilterBtn').on('click',function(){
        var _filterobj={};
        var _minPrice=$('#maxPrice').attr('min');
        var _maxPrice=$('#maxPrice').val();
        _filterobj._minPrice=_minPrice;
        _filterobj._maxPrice=_maxPrice;
       
        $('.filter-checkbox').each(function(index,ele){
            var _filterVal=$(this).val();
            var _filterKey=$(this).data('filter');
            _filterobj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
                return el.value;
           });
        });
        
        // run ajax 
        $.ajax({
            url:'filter-data/',
            data:_filterobj,
            dataType:'json',
            beforeSend:function(){
                $('#filter-product').html('loading');
            },
            success:function(res){
                $('#filter-product').html(res.products);
                console.log("ok")
                console.log(res);
            }
        });
    });

    // end 
    $("#maxPrice").on('blur',function(){
    
        var _min=$(this).attr('min');
        var _max=$(this).attr('max');
        var _value=$(this).val();
        console.log(_min,_max,_value)
        if (_value<parseInt(_min)|| _value>parseInt(_max)){
            alert("Values should be" +_min +'-'+_max);
            $(this).val(_min)
            $(this).focus();
            $('#RangeInput').val(_min);
            return false;

        }
    });
});

