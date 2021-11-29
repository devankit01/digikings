$(document).ready(function(){
    console.log("hwllo")
    const one=document.getElementById('1')
    const two=document.getElementById('2')
    const three=document.getElementById('3')
    const four=document.getElementById('4')
    const five=document.getElementById('5')
    var Review_alert_id=document.getElementById('Review_alert');
    const arr=[one,two,three,four,five]
    const handleSelect=(selection)=>{
        switch(selection){
                case '1' : {
                    one.classList.add('checked')
                    two.classList.remove('checked')
                    three.classList.remove('checked')
                    four.classList.remove('checked')
                    five.classList.remove('checked')
                    
                    return 
                }
                case '2' : {
                    one.classList.add('checked')
                    two.classList.add('checked')
                    three.classList.remove('checked')
                    four.classList.remove('checked')
                    five.classList.remove('checked')
                    return 
                }
                case '3' : {
                    one.classList.add('checked')
                    two.classList.add('checked')
                    three.classList.add('checked')
                    four.classList.remove('checked')
                    five.classList.remove('checked')
                    return 
                
                }
                case '4' : {
                    one.classList.add('checked')
                    two.classList.add('checked')
                    three.classList.add('checked')
                    four.classList.add('checked')
                    five.classList.remove('checked')
                    return 
                }
                case '5' : {
                    one.classList.add('checked')
                    two.classList.add('checked')
                    three.classList.add('checked')
                    four.classList.add('checked')
                    five.classList.add('checked')
                    return 
                }
        }

    }
    var ratingsId="";
    arr.forEach(item=>item.addEventListener('mouseover',(event)=>{
        handleSelect(event.target.id)
        

    }))
    arr.forEach(item=>item.addEventListener('click',(event)=>{
        ratingsId=event.target.id;
        main=document.getElementById(ratingsId)
        
    }))

    console.log(ratingsId)
    // review save section
    $('#addForm').submit(function(e){
        var _vm=$(this);
        console.log('submi')
        console.log($('#message').val())
        console.log(ratingsId)
        $.ajax({
            method:$(this).attr('method'),
            url:$(this).attr('action'),
            data:{
                'message':$('#message').val(),
                'ratings':ratingsId,
                'csrfmiddlewaretoken':$( "input[name='csrfmiddlewaretoken']" ).val(),
            },   
            dataType:'json',

            success:function(res){
                _vm.attr('disabled',false);
                $('.ajaxRes').html("successfully stored");
                $('#productReview').modal('toggle');
                $('#Add_reviewBtn').hide();
                Add_review_list(res.data);
                Review_alert_id.classList.remove('d-none')
                setTimeout(function(){
                    Review_alert_id.classList.add('d-none')
                },10000)
                // $('#reset').trigger('click');
            }
        })
        e.preventDefault();
    });


    // add _review _list live :
    const Add_review_list=(data)=>{
    
        var _html='<blockquote class="blockquote text-end">';
        _html += ' <small >'+data.review_text+'</small>';
        _html+='</blockquote>';
        _html += '<footer class="blockquote-footer ">'+data.first_name;
        _html += '<cite title="Source Title">';
        for (var i=0; i<data.review_rating;i++){
        _html += '<i class="fa fa-star text-warning"></i>';
        }
        _html += '</cite>';
        _html += ' </footer>';
        _html += '</figure>';
        _html += '<hr />';
        $('.review-list').prepend(_html);
    }
    

});