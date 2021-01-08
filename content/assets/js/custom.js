jQuery(function ($) {

    'use strict';
    var user_name = '';
    var invite_user_array = [];
    var is_location = false;
   
// ----------------------------------------------------------------
   


    (function() {

        var currentPage = 1;
        var pagenum = 1;

       function get_tickets()
       {           
           var data = $("#pagination-form").serialize();
            $.ajax({
                url: "/get_tickets",
                method: 'get',
                type: 'json',
                data: data,
                success: function(response) 
                {
                    $(".ticket_list").html("");
                    if(response.results.length > 0)
                    {
                        var data = response.results; 
                        pagenum = response.pagenum;
                        $(".total-page").html(pagenum);  
                        $(".ticket_list").html("");
                        for (var i = 0; i < data.length; i++) {
                            data[i];
                            var html = `
                                <tr>
                                    <td>
                                        ${(currentPage-1)*10+i+1}
                                    </td>
                                    <td>
                                        ${data[i].username}
                                    </td>
                                    <td>
                                        ${data[i].bookie}
                                    </td>
                                    <td>
                                        ${data[i].license_key}
                                    </td>
                                    <td>
                                        ${data[i].count}
                                    </td>
                                    <td>
                                        ${data[i].created_at}
                                    </td>
                                    <td>
                                        ${data[i].expire}
                                    </td>   
                                    <td>
                                        
                                    </td>                                 
                                    <td width="250">                                       
                                        <a class="btn_transparent btn_edit_ticket text-green mr-2" title="Edit" href="/edit/${data[i].id}" data-id="${data[i].id}">
                                            <i class="far fa-edit"></i>
                                        </a>
                                        <button type="buttom" title="Pause" class="btn_transparent btn_pause_ticket text-blue mr-2" data-id="${data[i].id}">
                                            <i class="fas fa-pause"></i>
                                        </button>
                                        <button type="buttom" title="Delete" class="btn_transparent btn_delete_ticket text-red" data-id="${data[i].id}">
                                            <i class="far fa-trash-alt"></i>
                                        </button>
                                    </td>
                                </tr>
                            `;
                            $(".ticket_list").append(html);
                        }
                        

                    }
                    else
                    {
                        var html = `
                                <tr>
                                    <td class="text-center" colspan="15">
                                        <p>There is no any ticket yet.</p>
                                    </td>                                   
                                </tr>
                            `;
                            $(".ticket_list").append(html);
                    }
                }
            });
       }

        
       $(document).on('click','.btn_create_ticket',function()
       {            
            var checkvalid = true;       
            $(".required").each(function(){
                if($(this).val() == "")
                {                        
                    $(this).addClass('alertborder');
                    checkvalid = false;
                }
            });
            
            if(checkvalid)
            {
                var data = $("#form_ticket").serialize();
                $.ajax({
                    url: "/store",
                    method: 'post',
                    type: 'json',
                    data: data,
                    success: function(response) 
                    {
                        if(response.results)
                        {
                            swal({
                                title: "Successfully stored!",                                                                                
                                type: "success"
                            }).then(function() {
                                location.reload()
                            });
                        }
                        else if(!response.is_username)
                        {
                            swal({
                                title: "Username is exsist already!",                                                                                
                                type: "error",
                                text: "Please try another."
                            }).then(function() {
                                
                            });
                        }
                        else
                        {
                            swal({
                                title: "Something wrong!",                                                                                
                                type: "error"
                            }).then(function() {
                                location.reload()
                            });
                        }
                    }
                });
            }
        });

        $(document).on('click','.btn_delete_ticket',function(){
            var id = $(this).data('id');

            $.ajax({
                url: "/delete",
                method: 'GET',
                type: 'json',
                data: {id:id},
                success: function(response) 
                {
                    if(response.results)
                    {
                        swal({
                            title: "Successfully removed!",                                                                                
                            type: "success"
                        }).then(function() {
                            location.reload()
                        });
                    }
                    else
                    {
                        swal({
                            title: "Something wrong!",                                                                                
                            type: "error",
                            text: "Please try again",
                        }).then(function() {
                            location.reload()
                        });
                    }          
                }
            });
        });
        
        
        
        $(document).on('click','.alertborder',function(){
            $(this).removeClass('alertborder');
        });
        $(document).on('click','.btn_filter_clear',function(){
            location.reload();
        });
        $(document).on('click','.btn_filter',function(){
            get_tickets();
        });
        $(document).ready(function(){            
            $(".btn-current-page").html(currentPage);
            $("#currentPage").val(currentPage);
            $(".total-page").html(pagenum);
            get_tickets();     
        });   
        


        $(document).on('click','.btn-next',function(){                    
            if(currentPage==pagenum)
            {                        
                return false;
            }
            currentPage++;
            $(".btn-current-page").html(currentPage);
            $("#currentPage").val(currentPage);
            get_tickets();
        });
        $(document).on('click','.btn-prev',function(){
            if(currentPage==1)
            {                        
                return false;
            }
            currentPage--;
            $(".btn-current-page").html(currentPage);
            $("#currentPage").val(currentPage);
            get_tickets();
        });
        $(document).on('click','.btn-start',function(){
            currentPage = 1;
            $(".btn-current-page").html(currentPage);
            $("#currentPage").val(currentPage);
            get_tickets();
        });
        $(document).on('click','.btn-end',function(){
            currentPage = pagenum;
            $(".btn-current-page").html(currentPage);
            $("#currentPage").val(currentPage);
            get_tickets();
        });

    }());

 

  
   
});


    

