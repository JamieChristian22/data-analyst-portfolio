"""Explicit source contracts. Source data are simulated, not production records."""
PROJECTS = {
 '01_SaaS_Product_Analytics_StreamFlow': {
  'users': ('user_id', 'user_id:i signup_date:d country:s acquisition_channel:s plan_tier:s'),
  'subscriptions': ('user_id', 'user_id:i plan_tier:s mrr:f seats:i completed_step2:b churned_within_90d:b first_payment_date:d'),
  'events': (None, 'user_id:i event_date:d event_group:s event_name:s')},
 '02_AB_Test_Feature_Impact': {
  'ab_sessions': ('session_id', 'session_id:i session_date:d variant:s device:s source:s converted:b engagement_score:f bounce:b revenue:f')},
 '03_Ecommerce_Product_Analytics': {
  'web_sessions': ('session_id', 'session_id:i session_date:d device:s channel:s added_to_cart:b purchased:b'),
  'orders': ('session_id', 'session_id:i session_date:d device:s channel:s sku:s category:s discount_applied:b order_value:f units:i')},
 '04_Amazon_Marketplace_Analytics': {
  'listings': ('listing_id', 'listing_id:i seller_id:i category:s price:f rating:f in_stock:b'),
  'sales': (None, 'sale_date:d listing_id:i units_sold:i seller_id:i price:f rating:f in_stock:b category:s revenue:f')},
 '05_User_Journey_Analytics': {
  'users': ('user_id', 'user_id:i first_seen_date:d traffic_source:s device:s is_returning:b'),
  'journey_events': (None, 'user_id:i event_date:d journey_stage:s stage_order:i')}
}
STAGES = ['Landing','Browse','Product View','Add to Cart','Checkout','Purchase']
ONBOARDING = ['Step 1: Account','Step 2: Workspace','Step 3: Integration','Step 4: First Workflow','Step 5: Invite Team']
