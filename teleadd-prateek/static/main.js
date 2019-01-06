$(document).ready(function(){
  var grp1_len = $('.users1:last').attr('id');
  var grp1_c_page = 1;
  var grp1_t_page = 1;
  var grp1_name = $('#grp1').attr('grpname');

  var grp2_len = $('.users2:last').attr('id');
  var grp2_c_page = 1;
  var grp2_t_page = 1;
  var grp2_name = $('#grp2').attr('grpname');

  var c = 0;
  var addedUser = [];
  
  $('#grp1 span').text('(Total Members: '+grp1_len+')');
  $('#grp2 span').text('(Total Members: '+grp2_len+')');

  $("#grp1table tr").hide();
  $("#grp1table tr:lt(20)").show();

  $("#grp2table tr").hide();
  $("#grp2table tr:lt(20)").show();



  grp1_t_page = parseInt(Number(grp1_len)/20);
  if(grp1_t_page==0){
    grp1_t_page = 1
  }
  $('#grp1total').text("Total Pages: "+grp1_t_page);

  grp2_t_page = parseInt(Number(grp2_len)/20);
  if(grp2_t_page==0){
    grp2_t_page = 1
  }
  $('#grp2total').text("Total Pages: "+grp2_t_page);

  $('.tleft').click(function(){
    if(grp1_c_page>1){
      $("#grp1table tr").hide();
      $('.pageno').text(--grp1_c_page);
      var p = grp1_c_page*20;
      $("#grp1table tr:lt("+p+")").show();
      $("#grp1table tr:lt("+(p-20)+")").hide();
    }
  });

  $('.tright').click(function(){
    if(grp1_c_page<=grp1_t_page){
      $('.pageno').text(++grp1_c_page);
      var p = grp1_c_page*20;
      $("#grp1table tr:lt("+p+")").show();
      $("#grp1table tr:lt("+(p-20)+")").hide();
    }
  });

  $('.tleft2').click(function(){
    if(grp2_c_page>1){
      $("#grp2table tr").hide();
      $('.pageno2').text(--grp2_c_page);
      var p = grp2_c_page*20;
      $("#grp2table tr:lt("+p+")").show();
      $("#grp2table tr:lt("+(p-20)+")").hide();
    }
  });
  $('.tright2').click(function(){
    if(grp2_c_page<=grp2_t_page){
      $('.pageno2').text(++grp2_c_page);
      var p = grp2_c_page*20;
      $("#grp2table tr:lt("+p+")").show();
      $("#grp2table tr:lt("+(p-20)+")").hide();
    }
  });
/*
  $('.adduser').click(function(){
    var flg = 1;
    var user = $(this).attr('user');
    for(i=0;i<addedUser.length;i++){
      if(addedUser[i]==user){
        flg=0;
        break;
      }
    }
    if(flg==1){
      addedUser.push(user);
      $('.addedUser').append('<tr><td>'+(++c)+'.</td><td>'+user+'</td><td><button user="'+user+'" class="btn btn-danger removeuser">Remove</button></td></tr>');
    }else{
      alert('already added');
    }
  });

  $(document).on('click', '.removeuser', function(){
    var user = $(this).attr('user');
    $(this).parent().parent().remove();
    addedUser.pop('user');
  });
*/
  $(document).on('click', '.adduser', function(){
    var user = $(this).attr('user');
    $.get('http://ec2-52-66-248-85.ap-south-1.compute.amazonaws.com:9003/api/apponeuser/'+user+'/'+grp1_name, function(data){
      console.log(data);
      if(data>0){
        var username = $(this).attr('username');
        var status = $(this).attr('status');
        $('.addedUser').append('<tr><td>'+(++grp2_len)+'</td><td>'+username+'</td><td>'+status+'</td></tr>');
      }else{
        alert('Privacy Issue or Already Added');
      }
    });

  });


});
