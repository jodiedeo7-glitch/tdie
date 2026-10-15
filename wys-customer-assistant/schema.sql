-- WYS customer workspace. Apply only to a separately provisioned Cloudflare D1 binding WYS_DB.
CREATE TABLE IF NOT EXISTS wys_customers (
  id TEXT PRIMARY KEY,
  email TEXT NOT NULL UNIQUE,
  entitlement_source TEXT NOT NULL,
  entitlement_reference TEXT NOT NULL,
  verified_at TEXT NOT NULL,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS wys_preferences (
  customer_id TEXT PRIMARY KEY REFERENCES wys_customers(id),
  schema_version INTEGER NOT NULL DEFAULT 1,
  preferences_json TEXT NOT NULL,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS wys_looks (
  id TEXT PRIMARY KEY,
  customer_id TEXT NOT NULL REFERENCES wys_customers(id),
  status TEXT NOT NULL DEFAULT 'DRAFT',
  payload_json TEXT NOT NULL DEFAULT '{}',
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS wys_looks_customer_idx ON wys_looks(customer_id);
