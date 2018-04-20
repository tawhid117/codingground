/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package entryform;

import au.com.bytecode.opencsv.CSVReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.PrintWriter;
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.GridPane;
import javafx.scene.paint.Color;
import javafx.scene.paint.Paint;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.scene.text.TextAlignment;
import javafx.stage.Stage;
import javax.swing.JOptionPane;

/**
 *
 * @author Tawhid
 */
public class EntryForm extends Application {
    
    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("ENTRY FORM");
        
        
        
        GridPane grid = new GridPane();
        grid.setAlignment(Pos.CENTER);
        grid.setHgap(10);
        grid.setVgap(15);
        grid.setPadding(new Insets(25,25,25,25));
        
        Label label_heading = new Label("Entry Form");
        label_heading.setFont(Font.font("Comic Sans MS", FontWeight.EXTRA_BOLD, 25));
        label_heading.setTextFill(Paint.valueOf("red"));
        label_heading.setTextAlignment(TextAlignment.RIGHT);
        grid.add(label_heading, 1, 0);
        
        
        Label label_first_name = new Label ("First Name: ");
        label_first_name.setFont(Font.font("Times New Roman", 20));
        grid.add(label_first_name, 0, 0+2);
        label_first_name.setAlignment(Pos.TOP_LEFT);
        TextField text_first_name = new TextField();
        grid.add(text_first_name,1,0+2);
        
        Label label_last_name = new Label ("Last Name: ");
        label_last_name.setFont(Font.font("Times New Roman", 20));
        grid.add(label_last_name, 2, 0+2);
        label_first_name.setAlignment(Pos.TOP_LEFT);
        TextField text_last_name = new TextField();
        //text_last_name.setPrefWidth(300);
        grid.add(text_last_name,3,0+2);
            
        
        
        Label label_name_validity = new Label ("");
        label_name_validity.setTextFill(Color.RED);
        grid.add(label_name_validity,4,0+2,2,1);
        
        
        Label label_address = new Label ("Address: ");
        label_address.setFont(Font.font("Times New Roman", 20));
        grid.add(label_address, 0, 1+2);
        TextField text_address = new TextField();
        text_address.setPrefWidth(300);
        grid.add(text_address,1,1+2,3,1);
        
        Label label_phone = new Label ("Phone No.: ");
        label_phone.setFont(Font.font("Times New Roman", 20));
        grid.add(label_phone, 0, 2+2);
        TextField text_phone = new TextField();
        grid.add(text_phone,1,2+2);
        Label label_phone_validiy = new Label(".");
        grid.add(label_phone_validiy, 2, 2+2, 2, 1);
        label_phone_validiy.setTextFill(Color.RED);
       
        Label label_username = new Label("Pick username: ");
        label_username.setFont (Font.font("Times New Roman", 20) );
        grid.add(label_username, 0, 3+2);
        TextField text_username = new TextField();
        grid.add(text_username,1, 3+2);
        Label label_username_validity = new Label ("");
        grid.add(label_username_validity,3,3+2);
        Button button_check_username = new Button("Check Availability");
        button_check_username.setTextAlignment(TextAlignment.CENTER);
        grid.add(button_check_username, 2, 3+2, 2, 1);
        Label label_check_username = new Label(" --- ");
        grid.add(label_check_username, 3,3+2,2,1);
        label_check_username.setVisible(false);
        label_check_username.setTextFill(Color.RED);
        
        
        
        button_check_username.setOnAction(new EventHandler<ActionEvent>() {
           @Override
           public void handle(ActionEvent e){
               boolean username_availability = false;
               System.out.println(text_username.getText());
               username_availability = isUsernameAvailable(text_username.getText() );
               label_check_username.setVisible(true);
               if (isUsernameLegal(text_username.getText())){
                    if(text_username.getText()!="" && username_availability){ 
                        label_check_username.setText("   This username is available !");
                    }
                    else{
                        label_check_username.setText("   Taken !");
                    }
                }
               else if(!isUsernameLegal(text_username.getText())){
                    label_check_username.setText("   Please select a username without spaces and with only letters and numbers.");
                }
               if(!isLabelNameValid(text_first_name.getText(),text_last_name.getText() )   ){label_name_validity.setText("Please use only letters and spaces.");}
               else if (isLabelNameValid(text_first_name.getText(), text_last_name.getText() )){label_name_validity.setText("Ok");}
               
               if(!isPhoneValid(text_phone.getText() )   ){label_phone_validiy.setText("Please use numbers only.");}
               else if (isPhoneValid(text_phone.getText() )){label_phone_validiy.setText("Ok");}
           }
        } ) ;
        
        Label label_pass1 = new Label ("Enter Password: ");
        label_pass1.setFont(Font.font("Times New Roman", 20));
        grid.add(label_pass1, 0, 4+2);
        PasswordField text_pass1 = new PasswordField();
        grid.add(text_pass1, 1, 4+2);
        
        Label label_pass2 = new Label ("Re-enter: ");
        label_pass2.setFont(Font.font("Times New Roman", 20));
        grid.add(label_pass2, 0, 5+2);
        PasswordField text_pass2 = new PasswordField();
        grid.add(text_pass2, 1, 5+2);
        
        Button button_submit = new Button("Submit Data");
        button_submit.setTextAlignment(TextAlignment.CENTER);
        grid.add(button_submit, 0, 6+2);
        Label label_submit = new Label("");
        label_submit.setTextFill(Color.RED);
        grid.add(label_submit, 1, 6+2, 2, 1);
        
        
        button_submit.setOnAction(new EventHandler<ActionEvent>() {
           @Override
           public void handle(ActionEvent e){
           
           text_address.setText(text_address.getText().replaceAll(",", ".") );
           if (!isPassMatched(text_pass1.getText(), text_pass2.getText())){
               label_submit.setText("Passwords do not match !");
           }    
           else if(text_pass1.getText()=="" && text_pass2.getText()==""){
               label_submit.setText("You cannot add record without setting a password !");
           }    
           else if ( isUsernameLegal(text_username.getText() ) && isLabelNameValid(text_first_name.getText(),text_last_name.getText() ) &&  isPhoneValid(text_phone.getText() ) && text_pass1.getText()!= "" && text_pass2.getText() != "" && isPassMatched(text_pass1.getText(), text_pass2.getText()) ){
               
               
               add_record(text_username.getText(), text_first_name.getText(), text_last_name.getText(), text_address.getText(), text_phone.getText());
               label_submit.setText("Record added !");
               add_up(text_username.getText(), text_pass1.getText());
               
            System.out.println("!!!");
        }
             
           }
        } ) ;
        
        Button button_clear = new Button("Clear Fields");
        button_clear.setTextAlignment(TextAlignment.CENTER);
        grid.add(button_clear, 3, 6+2);
        
        button_clear.setOnAction(new EventHandler<ActionEvent>() {
           @Override
           public void handle(ActionEvent e){
               
           text_username.setText(""); text_first_name.setText(""); text_last_name.setText(""); text_address.setText(""); text_phone.setText("");text_pass1.setText("");text_pass2.setText("");
           label_check_username.setText(""); label_name_validity.setText(""); label_phone_validiy.setText(""); label_username_validity.setText("");label_submit.setText("");
           }
        } ) ;
        
        Scene scene = new Scene(grid, 1000, 400); // window size
        primaryStage.setScene(scene);
        
        primaryStage.show();
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        launch(args);
    }
 
    public static boolean isUsernameAvailable (String username){

        String file = "up.csv";
        boolean availability = true;
        CSVReader reader = null;
        try {
            reader = new CSVReader(new FileReader(file));
            String[] line;
            while ((line = reader.readNext()) != null) {
                if (username.equals(line[0])){
                    System.out.println("Duplicate username");
                    availability = false;
                }
            }
        } 
        catch (Exception e) {
              System.out.println(e);
        }
    return availability;    
    }
    public static boolean isUsernameLegal (String username){
        boolean legality = true;
        legality = username.matches("[a-zA-Z0-9]+");
    return legality;    
    }
    public static boolean isLabelNameValid (String first_name, String last_name){
        boolean legality = true;
        legality = first_name.matches("[a-zA-Z ]+") && last_name.matches("[a-zA-Z ]+");
    return legality;    
    }
    public static boolean isPhoneValid (String phone){
        boolean legality = true;
        legality = phone.matches("[0-9]+");
    return legality;    
    }
    public static boolean isPassMatched (String pass1, String pass2){
        boolean legality = false;
        if (pass1.equals(pass2)){legality = true;}
    return legality;    
    }
    
    public static void add_record(String text_username, String text_first_name, String text_last_name, String text_address, String text_phone){
        try
        {
            String path = "userdata.csv";
            FileWriter fw = new FileWriter(path, true);
            BufferedWriter bw = new BufferedWriter(fw);
            PrintWriter pw = new PrintWriter(bw); // 
            
            pw.println(text_username+","+text_first_name+","+text_last_name+","+text_address+","+text_phone+",");
            pw.flush(); // make sure that all data is written to file
            pw.close();
        
            JOptionPane.showMessageDialog(null, "record saved");
        }catch(Exception E)
        {
            System.out.println(E);
        }
    }
    
    public static void add_up(String text_username, String text_pass1){
        try
        {
            String path = "up.csv";
            FileWriter fw = new FileWriter(path, true);
            BufferedWriter bw = new BufferedWriter(fw);
            PrintWriter pw = new PrintWriter(bw); // 
            
            pw.println(text_username+","+text_pass1+",");
            pw.flush(); // make sure that all data is written to file
            pw.close();
        
        }catch(Exception E)
        {
            System.out.println(E);
        }
    
    }
    
    
}
