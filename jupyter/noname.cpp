///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jun 17 2015)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

MyFrame2::MyFrame2( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	wxBoxSizer* bSizer1;
	bSizer1 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText1 = new wxStaticText( this, wxID_ANY, wxT("MyLabel"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText1->Wrap( -1 );
	bSizer1->Add( m_staticText1, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_bitmap1 = new wxStaticBitmap( this, wxID_ANY, wxNullBitmap, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer1->Add( m_bitmap1, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_gauge1 = new wxGauge( this, wxID_ANY, 100, wxDefaultPosition, wxDefaultSize, wxGA_HORIZONTAL );
	m_gauge1->SetValue( 0 ); 
	bSizer1->Add( m_gauge1, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_bitmap2 = new wxStaticBitmap( this, wxID_ANY, wxNullBitmap, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer1->Add( m_bitmap2, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	wxBoxSizer* bSizer2;
	bSizer2 = new wxBoxSizer( wxHORIZONTAL );
	
	wxArrayString m_choice1Choices;
	m_choice1 = new wxChoice( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, m_choice1Choices, 0 );
	m_choice1->SetSelection( 0 );
	bSizer2->Add( m_choice1, 0, wxALL|wxALIGN_CENTER_VERTICAL, 5 );
	
	m_button1 = new wxButton( this, wxID_ANY, wxT("Sync"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer2->Add( m_button1, 0, wxALL|wxALIGN_CENTER_VERTICAL, 5 );
	
	
	bSizer1->Add( bSizer2, 1, wxALIGN_CENTER_HORIZONTAL, 5 );
	
	wxBoxSizer* bSizer3;
	bSizer3 = new wxBoxSizer( wxHORIZONTAL );
	
	wxBoxSizer* bSizer4;
	bSizer4 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText2 = new wxStaticText( this, wxID_ANY, wxT("MyLabel"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText2->Wrap( -1 );
	bSizer4->Add( m_staticText2, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_slider2 = new wxSlider( this, wxID_ANY, 50, 0, 100, wxDefaultPosition, wxDefaultSize, wxSL_VERTICAL );
	bSizer4->Add( m_slider2, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_checkBox1 = new wxCheckBox( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer4->Add( m_checkBox1, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	
	bSizer3->Add( bSizer4, 1, wxALIGN_CENTER_VERTICAL, 5 );
	
	wxBoxSizer* bSizer41;
	bSizer41 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText21 = new wxStaticText( this, wxID_ANY, wxT("MyLabel"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText21->Wrap( -1 );
	bSizer41->Add( m_staticText21, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_slider21 = new wxSlider( this, wxID_ANY, 50, 0, 100, wxDefaultPosition, wxDefaultSize, wxSL_VERTICAL );
	bSizer41->Add( m_slider21, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_checkBox11 = new wxCheckBox( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer41->Add( m_checkBox11, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	
	bSizer3->Add( bSizer41, 1, wxALIGN_CENTER_VERTICAL, 5 );
	
	wxBoxSizer* bSizer42;
	bSizer42 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText22 = new wxStaticText( this, wxID_ANY, wxT("MyLabel"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText22->Wrap( -1 );
	bSizer42->Add( m_staticText22, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_slider22 = new wxSlider( this, wxID_ANY, 50, 0, 100, wxDefaultPosition, wxDefaultSize, wxSL_VERTICAL );
	bSizer42->Add( m_slider22, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_checkBox12 = new wxCheckBox( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer42->Add( m_checkBox12, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	
	bSizer3->Add( bSizer42, 1, wxALIGN_CENTER_VERTICAL, 5 );
	
	wxBoxSizer* bSizer43;
	bSizer43 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText23 = new wxStaticText( this, wxID_ANY, wxT("MyLabel"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText23->Wrap( -1 );
	bSizer43->Add( m_staticText23, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_slider23 = new wxSlider( this, wxID_ANY, 50, 0, 100, wxDefaultPosition, wxDefaultSize, wxSL_VERTICAL );
	bSizer43->Add( m_slider23, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_checkBox13 = new wxCheckBox( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer43->Add( m_checkBox13, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	
	bSizer3->Add( bSizer43, 1, wxALIGN_CENTER_VERTICAL, 5 );
	
	wxBoxSizer* bSizer44;
	bSizer44 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText24 = new wxStaticText( this, wxID_ANY, wxT("MyLabel"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText24->Wrap( -1 );
	bSizer44->Add( m_staticText24, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_slider24 = new wxSlider( this, wxID_ANY, 50, 0, 100, wxDefaultPosition, wxDefaultSize, wxSL_VERTICAL );
	bSizer44->Add( m_slider24, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_checkBox14 = new wxCheckBox( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer44->Add( m_checkBox14, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	
	bSizer3->Add( bSizer44, 1, wxALIGN_CENTER_VERTICAL, 5 );
	
	wxBoxSizer* bSizer45;
	bSizer45 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText25 = new wxStaticText( this, wxID_ANY, wxT("MyLabel"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText25->Wrap( -1 );
	bSizer45->Add( m_staticText25, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_slider25 = new wxSlider( this, wxID_ANY, 50, 0, 100, wxDefaultPosition, wxDefaultSize, wxSL_VERTICAL );
	bSizer45->Add( m_slider25, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_checkBox15 = new wxCheckBox( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer45->Add( m_checkBox15, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	
	bSizer3->Add( bSizer45, 1, wxALIGN_CENTER_VERTICAL, 5 );
	
	wxBoxSizer* bSizer46;
	bSizer46 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText26 = new wxStaticText( this, wxID_ANY, wxT("MyLabel"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText26->Wrap( -1 );
	bSizer46->Add( m_staticText26, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_slider26 = new wxSlider( this, wxID_ANY, 50, 0, 100, wxDefaultPosition, wxDefaultSize, wxSL_VERTICAL );
	bSizer46->Add( m_slider26, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_checkBox16 = new wxCheckBox( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer46->Add( m_checkBox16, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	
	bSizer3->Add( bSizer46, 1, wxALIGN_CENTER_VERTICAL, 5 );
	
	wxBoxSizer* bSizer47;
	bSizer47 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText27 = new wxStaticText( this, wxID_ANY, wxT("MyLabel"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText27->Wrap( -1 );
	bSizer47->Add( m_staticText27, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_slider27 = new wxSlider( this, wxID_ANY, 50, 0, 100, wxDefaultPosition, wxDefaultSize, wxSL_VERTICAL );
	bSizer47->Add( m_slider27, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_checkBox17 = new wxCheckBox( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer47->Add( m_checkBox17, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	
	bSizer3->Add( bSizer47, 1, wxALIGN_CENTER_VERTICAL, 5 );
	
	
	bSizer1->Add( bSizer3, 1, wxEXPAND|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	
	this->SetSizer( bSizer1 );
	this->Layout();
	
	this->Centre( wxBOTH );
}

MyFrame2::~MyFrame2()
{
}
