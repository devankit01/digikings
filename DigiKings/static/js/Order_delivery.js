$(document).ready(function(){
    const _show_login_changes=document.getElementById('login_set')
    const _hide_login_changes=document.getElementById('login_change')
    const _show_Delivery_changes=document.getElementById('Delivery_set')
    const _hide_Delivery_changes=document.getElementById('Delivery_change')
    const _show_Order_summary_changes=document.getElementById('Order_sum_set')
    const _hide_Order_summary_changes=document.getElementById('Order_summary_change')
    const _hide_order_confirmation_summary=document.getElementById('Order_summary_confirmation')
    const _show_payment_options=document.getElementById('payment_options_set')
    const _hide_payment_changes=document.getElementById('Payment_options_change')
    const _payment_confirmation_btn=document.getElementById('Payment_confirm_btn')
    console.log(_hide_login_changes)
    $('#Change_btn_login').on('click',function(){
    
        _show_login_changes.classList.remove('d-none')
        _hide_login_changes.classList.add('d-none')
        _hide_Delivery_changes.classList.remove('d-none')
        _show_Delivery_changes.classList.add('d-none')
        _show_Order_summary_changes.classList.add('d-none')
        _hide_Order_summary_changes.classList.remove('d-none')
        _hide_order_confirmation_summary.classList.add('d-none')
        _show_payment_options.classList.add('d-none')
        _hide_payment_changes.classList.remove('d-none')

    });
    // Delivery Section
    $('#Continue_Login').on('click',function(){
        _show_Delivery_changes.classList.remove('d-none')
        _hide_Delivery_changes.classList.add('d-none')
        _show_login_changes.classList.add('d-none')
        _hide_login_changes.classList.remove('d-none')
        _show_Order_summary_changes.classList.add('d-none')
        _hide_Order_summary_changes.classList.remove('d-none')
        _hide_order_confirmation_summary.classList.add('d-none')
        _show_payment_options.classList.add('d-none')
        _hide_payment_changes.classList.remove('d-none')

    });
    $('#Delivery_here_btn').on('click',function(){
        _show_Delivery_changes.classList.add('d-none')
        _hide_Delivery_changes.classList.remove('d-none')
        _show_login_changes.classList.add('d-none')
        _hide_login_changes.classList.remove('d-none')
        _show_Order_summary_changes.classList.remove('d-none')
        _hide_Order_summary_changes.classList.add('d-none')
        _hide_order_confirmation_summary.classList.remove('d-none')
        _show_payment_options.classList.add('d-none')
        _hide_payment_changes.classList.remove('d-none')
    });
    $('#Confirmation_button').on('click',function(){
        
        _show_Delivery_changes.classList.add('d-none')
        _hide_Delivery_changes.classList.remove('d-none')
        _show_login_changes.classList.add('d-none')
        _hide_login_changes.classList.remove('d-none')
        _show_Order_summary_changes.classList.add('d-none')
        _hide_Order_summary_changes.classList.remove('d-none')
        _hide_order_confirmation_summary.classList.add('d-none')
        _show_payment_options.classList.remove('d-none')
        _hide_payment_changes.classList.add('d-none')
    });
    $('.flexRadioDefault1').on('click',function(){
        _payment_confirmation_btn.classList.remove('disabled')
    })
})