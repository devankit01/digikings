$(document).ready(function () {
    $('.filter-checkbox,#PriceFilterBtn').on('click', function () {
        var _filterobj = {};
        var _minPrice = $('#maxPrice').attr('min');
        var _maxPrice = $('#maxPrice').val();
        _filterobj._minPrice = _minPrice;
        _filterobj._maxPrice = _maxPrice;

        $('.filter-checkbox').each(function (index, ele) {
            var _filterVal = $(this).val();
            var _filterKey = $(this).data('filter');
            _filterobj[_filterKey] = Array.from(document.querySelectorAll('input[data-filter=' + _filterKey + ']:checked')).map(function (el) {
                return el.value;
            });
        });

        // run ajax 
        $.ajax({
            url: 'filter-data/',
            data: _filterobj,
            dataType: 'json',
            beforeSend: function () {
                $('#filter-product').html('loading');
            },
            success: function (res) {
                $('#filter-product').html(res.products);
                console.log("ok")
                console.log(res);
            }
        });
    });

    // end 
    // Price Filteration start
    $("#maxPrice").on('blur', function () {

        var _min = $(this).attr('min');
        var _max = $(this).attr('max');
        var _value = $(this).val();
        console.log(_min, _max, _value)
        if (_value < parseInt(_min) || _value > parseInt(_max)) {
            alert("Values should be" + _min + '-' + _max);
            $(this).val(_min)
            $(this).focus();
            $('#RangeInput').val(_min);
            return false;

        }
    });

    // Add to cart Start 
    $(document).on('click', '#addToCartBtn', function () {
        var _vm = $(this);
        var _Qty = $('#productQty').val();
        var _productId = $('.product-id').val();
        var _productTitle = $('.product-title').val();
        var _Price_product = $('#PriceProduct').text();
        var _productImage = $('.product-image').val();
        console.log(_Price_product);
        $.ajax({
            url: '/Add-to-cart',
            data: {
                'id': _productId,
                'qty': _Qty,
                'title': _productTitle,
                'Price': _Price_product,
                'image': _productImage,
            },
            dataType: 'json',
            beforeSend: function () {
                _vm.attr('disabled', true);
            },
            success: function (res) {
                $('.cart-list').text(res.totaItems);


                _vm.attr('disabled', false);
            }
        });

    });
    // end 
    // Delete item from cart
    $(document).on('click', '.delete-item', function () {
        console.log("hello");
        var _pid = $(this).attr('data-item');
        var _vm = $(this);
        $.ajax({
            url: '/Delete-Cart-item',
            data: {
                'id': _pid,

            },
            dataType: 'json',
            beforeSend: function () {
                _vm.attr('disabled', true);
            },
            success: function (res) {
                $('.cart-list').text(res.totaItems);
                $('#cartList').html(res.data);
                _vm.attr('disabled', false);
            }
        });
    });
    // end 
    // update item from item

    $(document).on('keyup change', '.update-item', function () {
        console.log("hello");
        var _pid = $(this).attr('data-item');
        console.log(_pid)
        var _vm = $(this);
        var _pQty = $('.product-qty-' + _pid).val();
        if (_pQty >= 1) {
            $.ajax({
                url: '/Update-Cart-item',
                data: {
                    'id': _pid,
                    'qty': _pQty
                },
                dataType: 'json',
                beforeSend: function () {
                    _vm.attr('disabled', true);
                },
                success: function (res) {

                    $('#cartList').html(res.data);
                    _vm.attr('disabled', false);
                }
            });
        }
        else{
            alert("quantity must be greater or equal than  1");
        }
    });

});

