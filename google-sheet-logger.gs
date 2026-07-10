/**
 * Chatbot Conversation Logger — Google Apps Script
 * 
 * SETUP (3 steps, 2 minutes):
 * 1. Open your Google Sheet: https://docs.google.com/spreadsheets/d/1U2cYT923K-y8uGJ-fHejF1073JDGj7zwr4vLbz_bk9U/edit
 * 2. Go to: Extensions → Apps Script
 * 3. Delete any code there, paste ALL of this code, then click Save
 * 4. Click: Deploy → New deployment
 *    - Type: Web app
 *    - Description: Chatbot logger
 *    - Execute as: Me (your email)
 *    - Who has access: Anyone
 *    - Click Deploy → Authorize → Allow
 * 5. Copy the URL (looks like https://script.google.com/macros/s/AKfyc.../exec)
 * 6. Paste it into chatbot.js line 24: const SHEET_WEBHOOK_URL = 'YOUR_URL_HERE'
 */

function doPost(e) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  
  // Add headers if sheet is empty
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(['Timestamp', 'Page', 'Language', 'Role', 'Message']);
    sheet.getRange(1, 1, 1, 5).setFontWeight('bold');
  }
  
  var data = JSON.parse(e.postData.contents);
  var timestamp = data.timestamp;
  var page = data.page;
  var language = data.language;
  
  data.conversation.forEach(function(msg) {
    sheet.appendRow([timestamp, page, language, msg.role, msg.text]);
  });
  
  // Separator row between conversations
  sheet.appendRow(['', '', '', '', '---']);
  
  return ContentService.createTextOutput('OK');
}
